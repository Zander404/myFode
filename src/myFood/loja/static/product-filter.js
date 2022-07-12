const filters = document.querySelector("#filters");

filters.addEventListener("input", filterGoods);

function filterGoods() {
  const country = filters.querySelector("#country").value,
    sizes = [...filters.querySelectorAll("#size input:checked")].map(
      (n) => n.value
    ),
    priceMin = document.querySelector("#price-min").value,
    priceMax = document.querySelector("#price-max").value;

  outputGoods(
    DATA.filter(
      (n) =>
        (!country || n.country === country) &&
        (!sizes.length || sizes.includes(n.size)) &&
        (!priceMin || priceMin <= n.cost) &&
        (!priceMax || priceMax >= n.cost)
    )
  );
}

function outputGoods(goods) {
  document.getElementById("goods").innerHTML = goods
    .map(
      (n) => `
    <div class="single-goods">
    <div class="border-2 border-gray-200 rounded-lg overflow-hidden mb-3">
      <div class="text-center">
      <h3 class"py-2 font-bold">${n.name}</h3>
      <img src="${n.image}" class="block mx-auto">
      <p class="font-bold py-4">Цена: ${n.cost}</p>
      
      <div class="overflow-hidden flex justify-center p-8">
  <button tabindex="-1" data-art="${n.name}" class="focus:outline-none w-32 py-2 rounded-md font-semibold text-white bg-indigo-500 ring-4 ring-indigo-300 hover:bg-indigo-700">
    Button
  </button>
</div>
      </div>
      </div>
    </div>
  `
    )
    .join("");
}

const DATA = [
  {
    sex: "male",
    name: "Рубашка №1",
    cost: 1000,
    country: "france",
    image:
      "http://i.piccy.info/i9/9921ed03bf45751d45447b15e78be751/1566814909/19890/1334636/1.jpg",
    size: "S"
  },
  {
    sex: "male",
    name: "Рубашка №2",
    cost: 1200,
    country: "turkey",
    image:
      "http://i.piccy.info/i9/acc4df9b14e48a42d7cd353e923673e7/1566814962/22015/1334636/2.jpg",
    size: "M"
  },
  {
    sex: "male",
    name: "Рубашка №3",
    cost: 1700,
    country: "china",
    image:
      "http://i.piccy.info/i9/174610be67bfea39f99c956885ae3786/1566815027/25896/1334636/3.jpg",
    size: "L"
  },
  {
    sex: "male",
    name: "Рубашка №4",
    cost: 2000,
    country: "turkey",
    image:
      "http://i.piccy.info/i9/e2e5c6cb274121b9898b7d45a085130f/1566815049/29582/1334636/4.jpg",
    size: "XL"
  }
];

outputGoods(DATA);
