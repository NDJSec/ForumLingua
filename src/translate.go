package main

import (
	"C"

	"bytes"
	"unsafe"

	"github.com/bregydoc/gtranslate"
)

//export translate
func translate(ut *C.char, sl *C.char, tl *C.char, out *byte, outN int64) *byte {
	outBytes := unsafe.Slice(out, outN)[:0]
	buf := bytes.NewBuffer(outBytes)

	var untraslatedText string = C.GoString(ut)
	var sourceLanguage string = C.GoString(sl)
	var targetLanguage string = C.GoString(tl)

	translated, err := gtranslate.TranslateWithParams(
		untraslatedText,
		gtranslate.TranslationParams{
			From: sourceLanguage,
			To:   targetLanguage,
		},
	)
	if err != nil {
		panic(err)
	}
	buf.WriteString(translated)
	buf.WriteByte(0)
	return out
}

func main() {}
