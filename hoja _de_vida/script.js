function downloadPDF(){

    const element = document.querySelector('#pdf-content');
    //console.log(element)

    const otp = {
        margin: [10, 5, 15, 5],  //[Arriba, Izquierda, Abajo, Derecha] en mm
        filename: 'Hoja_de_vida_Jose_Diaz.pdf',
        image: { type: 'jpeg', quality: 1 },
        
        html2canvas:{
            scale: 2,
            useCORS: true, // Permite traer imagenes de otro servidor
            scrollY: 0 // Para que no haya desplazamiento de la imagen
        },

        jsPDF: {
            unit: 'mm',
            format: 'A4',
            orientation: 'portrait' // Orientación vertical
        }
    }
    html2pdf().set(otp).from(element).save();
}