/**
 * Resim urllerini alma
 * @param {number} pageNum Sayfa sayısı
 */
function getImageUrls(pageNum) {
    pageNum = (pageNum === 0) ? 67 : pageNum;
    const urls = [];
    // Her saufa için tekrarlama. 
    // Not: Sayfa sayısı 1'den başlar
    for (let i = 1; i < pageNum; i++) {
        const articleCollection = document.getElementById("assets").getElementsByTagName('article');
        const articles = [...articleCollection];
        articles.forEach(article => {
            url = article.getAttribute("data-thumb-url");
            urls.push(url);
        });

        // Sonraki sayfaya geçme
        document.getElementById("next-gallery-page").click()
    }
    // urls.length;
    return urls;
}

// const link = document.createElement('a');
// link.href = url;
// link.download = 'file.jpg';
// link.dispatchEvent(new MouseEvent('click'));
// document.getElementById("assets").getElementsByTagName("article")[0].getAttribute("data-thumb-url")