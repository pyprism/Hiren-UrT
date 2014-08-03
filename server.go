package main

import (
	"github.com/go-martini/martini"
	"github.com/googollee/go-socket.io"
	"github.com/martini-contrib/render"
	"log"
)

func main() {
	m := martini.Classic()
	m.Use(render.Renderer())

	server, err := socketio.NewServer(nil)
	if err != nil {
		log.Fatal(err)
	}
	server.On("connection", func(so socketio.Socket) {
		log.Println("on connection")
		so.Join("chat")
		so.On("chat message", func(msg string) {
			log.Println("emit:", so.Emit("chat message", msg))
			so.BroadcastTo("chat", "chat message", msg)
		})
		so.On("disconnection", func() {
			log.Println("on disconnect")
		})
	})
	server.On("error", func(so socketio.Socket, err error) {
		log.Println("error:", err)
	})

	m.Get("/", func(r render.Render) {
		r.HTML(200, "index", "jeremy")
	})
	m.Run()
}
