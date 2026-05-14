<template>
  <div class="register-container">
    <h2>캠핑카 사용자 등록</h2>
    <form @submit.prevent="handleRegister">
      <!-- Name -->
      <div class="form-group">
        <label for="name">이름 (Name):</label>
        <input
          id="name"
          v-model="form.name"
          type="text"
          required
          placeholder="성명을 입력하세요"
        />
      </div>

      <!-- Address -->
      <div class="form-group">
        <label for="address">주소 (Address):</label>
        <input
          id="address"
          v-model="form.address"
          type="text"
          required
          placeholder="주소를 입력하세요"
        />
      </div>

      <!-- Phone Number -->
      <div class="form-group">
        <label for="phone">전화번호 (Phone Number):</label>
        <input
          id="phone"
          v-model="form.phone"
          type="tel"
          required
          placeholder="010-0000-0000"
        />
      </div>

      <!-- Previous Camping Car Usage Date -->
      <div class="form-group">
        <label for="previousUsageDate">이전 캠핑카 사용 날짜:</label>
        <input
          id="previousUsageDate"
          v-model="form.previousUsageDate"
          type="date"
        />
      </div>

      <!-- Previous Camping Car Type -->
      <div class="form-group">
        <label for="previousCarType">이전 사용 캠핑카 종류:</label>
        <select v-model="form.previousCarType">
          <option value="">선택하세요</option>
          <option value="motorhome">모토홈</option>
          <option value="trailer">트레일러</option>
          <option value="camper-van">캠퍼밴</option>
          <option value="rv">RV</option>
          <option value="other">기타</option>
        </select>
      </div>

      <!-- Submit Button -->
      <button type="submit" class="btn-register">등록 (Register)</button>
    </form>

    <!-- Display submitted data -->
    <div v-if="submittedData" class="submitted-data">
      <h3>등록된 정보:</h3>
      <p><strong>이름:</strong> {{ submittedData.name }}</p>
      <p><strong>주소:</strong> {{ submittedData.address }}</p>
      <p><strong>전화번호:</strong> {{ submittedData.phone }}</p>
      <p><strong>이전 캠핑카 사용 날짜:</strong> {{ submittedData.previousUsageDate || 'N/A' }}</p>
      <p><strong>이전 사용 캠핑카 종류:</strong> {{ submittedData.previousCarType || 'N/A' }}</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Register',
  data() {
    return {
      form: {
        name: '',
        address: '',
        phone: '',
        previousUsageDate: '',
        previousCarType: ''
      },
      submittedData: null
    };
  },
  methods: {
    handleRegister() {
      // Validate form
      if (!this.form.name || !this.form.address || !this.form.phone) {
        alert('필수 항목을 입력해주세요. (Please fill in all required fields)');
        return;
      }

      // Store submitted data
      this.submittedData = { ...this.form };

      // Log data to console
      console.log('Registered User Data:', this.submittedData);

      // You can send this data to a backend API here
      // Example:
      // this.$axios.post('/api/register', this.submittedData)
      //   .then(response => {
      //     console.log('Registration successful:', response);
      //     this.resetForm();
      //   })
      //   .catch(error => {
      //     console.error('Registration failed:', error);
      //   });

      // Reset form after successful registration
      // this.resetForm();
    },

    resetForm() {
      this.form = {
        name: '',
        address: '',
        phone: '',
        previousUsageDate: '',
        previousCarType: ''
      };
      this.submittedData = null;
    }
  }
};
</script>

<style scoped>
.register-container {
  max-width: 500px;
  margin: 40px auto;
  padding: 30px;
  border: 1px solid #ddd;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  font-family: Arial, sans-serif;
}

h2 {
  text-align: center;
  color: #333;
  margin-bottom: 30px;
}

.form-group {
  margin-bottom: 20px;
  display: flex;
  flex-direction: column;
}

label {
  margin-bottom: 8px;
  font-weight: bold;
  color: #555;
  font-size: 14px;
}

input,
select {
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
  font-size: 14px;
  font-family: inherit;
}

input:focus,
select:focus {
  outline: none;
  border-color: #4caf50;
  box-shadow: 0 0 5px rgba(76, 175, 80, 0.3);
}

.btn-register {
  width: 100%;
  padding: 12px;
  background-color: #4caf50;
  color: white;
  border: none;
  border-radius: 4px;
  font-size: 16px;
  font-weight: bold;
  cursor: pointer;
  transition: background-color 0.3s;
}

.btn-register:hover {
  background-color: #45a049;
}

.submitted-data {
  margin-top: 30px;
  padding: 20px;
  background-color: #f0f0f0;
  border-radius: 4px;
  border-left: 4px solid #4caf50;
}

.submitted-data h3 {
  margin-top: 0;
  color: #333;
}

.submitted-data p {
  margin: 10px 0;
  color: #555;
  line-height: 1.6;
}
</style>
