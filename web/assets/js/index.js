new Vue({
    el: "#app",
    data: {
        correct_result: "",
        display: "none",
        err_display: "none",
        text: "",
        lang: "",
    },
    methods: {
        async translate() {
            try {
                let translated_text = await eel.translate_text(this.lang, this.text)();
                // Добавьте () после eel.translate_text(this.lang, this.text)
                // для вызова функции

                if (translated_text == "Error") {
                    this.err_display = "block";
                } else {
                    this.display = "block";
                    this.correct_result = translated_text;
                }
            } catch (error) {
                console.error(error);
                this.err_display = "block";
            }
        },
    }
});
