package main

import (
	"fmt"
	"log"
	"os"
	"os/exec"

	"gopkg.in/ini.v1"
)

func main() {
	fmt.Println("Welcome to the Forum Linuga Launcher!")
	fmt.Println("Checking if dependencies are installed...")

	cfg, err := ini.Load("assets/ForumLingua.ini")
	if err != nil {
		log.Fatal(err)
	}

	if cfg.Section("requiredPackages").Key("ForumLinguaInstalled").MustBool() == false {
		fmt.Printf("ForumLingua not installed.\n INSTALLING...\n")

		if cfg.Section("requiredPackages").Key("pythonExecutable").MustBool() == false {
			pythonCmd := exec.Command("python", "--version")
			pyErr := pythonCmd.Run()

			if pyErr != nil {
				log.Fatal("Python not installed. Visit https://www.python.org/ to install")
			}
			cfg.Section("requiredPackages").Key("pythonExecutable").SetValue("true")
		}

		if cfg.Section("requiredPackages").Key("pythonDependencies").MustBool() == false {
			pythonCmd := exec.Command("python", "setup.py", "install")
			pyErr := pythonCmd.Run()

			if pyErr != nil {
				log.Fatal("Dependencies not installed. Check dependencies or contact maintainer")
			}
			cfg.Section("requiredPackages").Key("pythonDependencies").SetValue("true")
		}

		if cfg.Section("requiredPackages").Key("ForumLinguaDLLInstalled").MustBool() == false {
			_, fileError := os.Stat("src/translate.dll")
			if os.IsNotExist(fileError) {
				log.Fatal("translate.dll doesn't exsist check files and contact maintainer")
			}
			cfg.Section("requiredPackages").Key("ForumLinguaDLLInstalled").SetValue("true")
		}
		fmt.Println("ForumLingua Installed 😊")
		cfg.Section("requiredPackages").Key("ForumLinguaInstalled").SetValue("true")
		cfg.SaveTo("assets/ForumLingua.ini")
		cmd := exec.Command("ForumLingua")
		err := cmd.Run()

		if err != nil {
			log.Fatal(err)
		}

	} else {
		cmd := exec.Command("ForumLingua")
		err := cmd.Run()

		if err != nil {
			log.Fatal(err)
		}
	}
}
