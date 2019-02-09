/**
 * Resim urllerini alma
 * @param {number} pageNum Sayfa sayısı
 */
window.getImageUrls = function getImageUrls(pageNum) {
    pageNum = (typeof pageNum === 'undefined') ? 67 : pageNum;
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
};