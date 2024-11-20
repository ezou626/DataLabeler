function ConfirmationPage({ confirmationCode, moreTasks }) {
  return (
    <div className="max-w-lg mx-auto mt-10 p-6 bg-white shadow-lg rounded-md text-center">
      <h1 className="text-3xl font-bold mb-4 text-blue-600">Congrats on completing a task!</h1>
      <p className="text-gray-700 text-lg mb-6">
        Your confirmation code is: <span className="font-bold py-4">{confirmationCode}</span> Please record the code now. 
        Afterwards, follow the link to MTurk, and input the code along with your worker ID to claim
        your payment.
        
      </p>
      <div className="flex justify-center space-x-4">
        <button
          onClick={moreTasks}
          className="px-6 py-3 bg-blue-950 text-white font-semibold rounded-md hover:bg-blue-700 transition duration-200"
        >
          Complete Another Task
        </button>
      </div>
    </div>
  );
}

export default ConfirmationPage;
